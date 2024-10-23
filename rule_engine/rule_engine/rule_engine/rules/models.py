from django.db import models

class Node(models.Model):
    NODE_TYPES = [
        ('operator', 'Operator'),
        ('operand', 'Operand'),
    ]
    
    type = models.CharField(max_length=10, choices=NODE_TYPES)  # Operator or Operand
    operator = models.CharField(max_length=5, null=True, blank=True)  # AND, OR
    value = models.CharField(max_length=100, null=True, blank=True)   # For operands like 'age > 30'
    left = models.ForeignKey('self', null=True, blank=True, related_name='left_node', on_delete=models.CASCADE)
    right = models.ForeignKey('self', null=True, blank=True, related_name='right_node', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.type}: {self.operator or self.value}'
