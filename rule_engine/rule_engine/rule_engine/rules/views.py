from django.http import JsonResponse
from .models import Node
import json

# Helper to parse rule strings and create AST
def create_ast(rule_string):
    # Parse the rule string and convert it to an AST. (This is simplified for illustration)
    # Real implementation would involve parsing expressions correctly (e.g., using pyparsing).
    
    if 'AND' in rule_string or 'OR' in rule_string:
        operator = 'AND' if 'AND' in rule_string else 'OR'
        left, right = rule_string.split(operator)
        root_node = Node.objects.create(type='operator', operator=operator.strip())
        root_node.left = create_ast(left.strip())
        root_node.right = create_ast(right.strip())
        root_node.save()
        return root_node
    else:
        return Node.objects.create(type='operand', value=rule_string.strip())

# API view for creating a rule
def create_rule(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rule_string = data.get('rule', '')
        ast = create_ast(rule_string)
        return JsonResponse({'message': 'Rule created', 'rule_id': ast.id})

# API view for evaluating a rule
def evaluate_rule(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rule_id = data.get('rule_id')
        attributes = data.get('attributes')

        ast = Node.objects.get(id=rule_id)
        result = evaluate_ast(ast, attributes)
        return JsonResponse({'result': result})

# Recursive evaluation function
def evaluate_ast(node, attributes):
    if node.type == 'operand':
        # Process the operand, e.g., "age > 30"
        attribute, condition = node.value.split('>')
        return attributes.get(attribute.strip()) > int(condition.strip())
    
    elif node.type == 'operator':
        left_result = evaluate_ast(node.left, attributes)
        right_result = evaluate_ast(node.right, attributes)
        if node.operator == 'AND':
            return left_result and right_result
        elif node.operator == 'OR':
            return left_result or right_result

    return False
