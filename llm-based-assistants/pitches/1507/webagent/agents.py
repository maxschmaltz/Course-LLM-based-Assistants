from langchain_core.messages import AIMessage

from webagent.prompts import (
    SYSTEM_PROMPT,
    MAKE_UP_BIOGRAPHY_PROMPT,
    GENERATE_RESUME_PROMPT,
    VALIDATE_RESUME_PROMPT
)

# choose any model, catalogue is available under https://build.nvidia.com/models
MODEL_NAME = "meta/llama-3.3-70b-instruct"


class ResumeGenerator:

    def __init__(self, max_refinements: int=5, **kwargs):
        self.llm = ...

    def complete_biography(self, input_prompt: str) -> AIMessage:

        """
        Fill in the gaps in the character's biography:
        everything that is relevant for a resume, such as
        education, work experience, skills, etc.
        
        Args:
            input_prompt (str): The initial (partial) description of the character
            
        Returns:
            AIMessage: The completed biography of the character
        """

        pass
    
    def generate_resume(self, biography: str) -> AIMessage:

        """
        Generate HTML (and CSS) code for a one-page resume based on the character biography.
        
        Args:
            biography (str): The complete biography of the character
            
        Returns:
            AIMessage: The HTML (and CSS) code for the resume
        """

        pass
    
    def validate_resume(self, resume_code: str) -> bool:

        """
        Validate the generated HTML (and CSS) code for the resume.
        It should check if the HTML is well-formed and if the CSS styles are applied correctly.
        
        Args:
            resume_code (str): The HTML (and CSS) code for the resume
            
        Returns:
            bool: Whether the resume code is valid or not
        """
        pass
    
    def refine_resume_code(self, resume_code: str) -> AIMessage:
        
        """
        Refine the generated HTML (and CSS) code for the resume.
        It should fix technical errors in the code as well as
        change contents if they are not matching the biography.
        
        Args:
            resume_code (str): The HTML (and CSS) code for the resume
            
        Returns:
            AIMessage: The refined HTML (and CSS) code for the resume
        """
        pass

    def save_resume(self, resume_code: str) -> None:

        """
        Save the generated HTML (and CSS) code for the resume to a file.
        
        Args:
            resume_code (str): The HTML (and CSS) code for the resume
        """
        pass
    
    def run(self,query: str) -> AIMessage:

        """
        Run the agent with the given query.
        """

        pass