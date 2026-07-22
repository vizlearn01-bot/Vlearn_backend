import os
import django
import json
import sys

sys.path.append('/home/jason-bitega/Desktop/VL/repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from curriculum.models import LearningExperienceGraph

graph = LearningExperienceGraph.objects.order_by('-created_at').first()
if graph:
    print(json.dumps(graph.graph_data, indent=2))
else:
    print("No graph found")
