import os

import click
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DeepLake

from src.cli import pass_environment

@click.command("index", short_help="Index code to an ActivePool")
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode")
@click.option('-ua', '--username-activepool', required=True, help='Username ActivePool')
@click.option('-ds', '--dataset', required=False, help='Dataset name in ActivePool')
@click.option('-sp', '--source-path', required=False, help="Code source to upload")
@pass_environment
def cli(ctx, verbose, username_activepool, dataset, source_path):
    """
    Index the data source to an ActivePool Storage
    """
    ctx.verbose = verbose
    embeddings = OpenAIEmbeddings(disallowed_special=())
    root_dir = source_path
    docs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            try:
                loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
                docs.extend(loader.load_and_split())
            except Exception as e:
                pass

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(docs)
    db = DeepLake(
        dataset_path=f"hub://{username_activepool}/{dataset}",
        embedding_function=embeddings)  # dataset would be publicly available
    db.add_documents(texts)