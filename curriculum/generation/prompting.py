import json
from typing import List, Dict
from curriculum.models import GenerationRule

class PromptBuilder:
    @staticmethod
    def build_prompt(context_package: dict, rule: GenerationRule, previous_blocks: List[Dict]) -> str:
        prompt = f"System Instructions:\n{rule.system_prompt}\n\n"
        
        prompt += f"Educational Context:\n"
        prompt += f"- Curriculum: {context_package['curriculum']}\n"
        prompt += f"- Grade: {context_package['grade']}\n"
        prompt += f"- Subject: {context_package['subject']}\n"
        prompt += f"- Topic: {context_package['topic']}\n"
        prompt += f"- Learning Unit: {context_package['learning_unit']}\n\n"
        
        prompt += f"Approved Textbook Content:\n"
        chunks = context_package['chunks']
        
        if chunks['definitions']:
            prompt += "--- DEFINITIONS ---\n"
            for chunk in chunks['definitions']:
                prompt += f"- {chunk['content']} (Page {chunk['pages']})\n"
            prompt += "\n"
            
        if chunks['worked_examples']:
            prompt += "--- WORKED EXAMPLES ---\n"
            for chunk in chunks['worked_examples']:
                prompt += f"{chunk['content']} (Page {chunk['pages']})\n\n"
                
        if chunks['diagrams']:
            prompt += "--- DIAGRAMS & FIGURES ---\n"
            for chunk in chunks['diagrams']:
                prompt += f"- Figure [ID: {chunk.get('image_url', 'N/A')}] (Page {chunk['pages']})\n"
            prompt += "\n"
            
        if chunks['practicals']:
            prompt += "--- PRACTICALS / EXPERIMENTS ---\n"
            for chunk in chunks['practicals']:
                prompt += f"{chunk['content']} (Page {chunk['pages']})\n\n"
                
        if chunks['exercises']:
            prompt += "--- ASSESSMENT QUESTIONS ---\n"
            for chunk in chunks['exercises']:
                prompt += f"{chunk['content']} (Page {chunk['pages']})\n\n"
                
        if chunks['core_text']:
            prompt += "--- CORE TEXT ---\n"
            for chunk in chunks['core_text']:
                prompt += f"{chunk['content']} (Page {chunk['pages']})\n\n"
            
        if previous_blocks:
            prompt += f"Previously Generated Blocks (for continuity):\n"
            for b in previous_blocks:
                prompt += f"--- {b['block_type'].upper()} ---\n{b['content']}\n\n"
                
        prompt += "Based on the System Instructions and the Approved Textbook Content ONLY, please generate the required content. Output in Markdown format (or requested JSON schema) without any conversational filler."
        return prompt
