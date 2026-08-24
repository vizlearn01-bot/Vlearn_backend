import re
import os
from curriculum.bs_verified_images import VERIFIED_IMAGES

def process_file(filepath, topic_id):
    with open(filepath, 'r') as f:
        content = f.read()

    # We need to process each lesson separately to add the image to page 1
    # We will use regex to find the start of each lesson's pages
    # Let's find each LESSON_X_DATA and page_number: 1
    
    pass

