import os
import json
import requests
from typing import TypedDict, List, Optional

from langgraph.graph import StateGraph
from langchain_openai import AzureChatOpenAI
