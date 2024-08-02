from cmd import Cmd

import click
from langchain_community.vectorstores import DeepLake
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

from src.cli import pass_environment

class AuditAIPrompt(Cmd):

    def __init__(self, dataset_path):
        super(AuditAIPrompt, self).__init__()
        self.retriever = self.get_retriever(dataset_path=dataset_path)
        self.chat_history = []
            
    def get_retriever(self, dataset_path):
        embeddings = OpenAIEmbeddings(disallowed_special=())
        db = DeepLake(
            dataset_path=dataset_path,
            read_only=True,
            embedding_function=embeddings)  # use your username
        retriever = db.as_retriever()
        retriever.search_kwargs['distance_metric'] = 'cos'
        retriever.search_kwargs['fetch_k'] = 100
        # retriever.search_kwargs['maximal_marginal_relevance'] = True
        retriever.search_kwargs['k'] = 10
        return retriever

    def do_qa(self, args):
        model = ChatOpenAI(model_name='gpt-4o')
        conversation = ConversationalRetrievalChain.from_llm(model, retriever=self.retriever)
        result = conversation({"question": args, "chat_history": self.chat_history})
        self.chat_history.append((args, result['answer']))
        print(f"\n**Answer**: {result['answer']} \n")

    def do_exit(self, args):
        """
        Exit the prompt
        """
        raise SystemExit

@click.command("prompt", short_help="Prompt code")
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode")
@click.option('-ua', '--username-activepool', required=True, help='Username ActivePool')
@click.option('-ds', '--dataset', required=False, help='Dataset name in ActivePool')
@pass_environment
def cli(ctx, verbose, username_activepool, dataset):
    """
    Open prompt
    """
    ctx.verbose = verbose
    prompt = AuditAIPrompt(dataset_path=f"hub://{username_activepool}/{dataset}")
    prompt.prompt = '> '
    prompt.cmdloop('Starting conversation...')
