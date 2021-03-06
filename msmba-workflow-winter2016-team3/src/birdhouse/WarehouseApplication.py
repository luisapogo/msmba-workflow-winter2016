'''
The Barista User Interface for the coffee bar workflow (Winter Intensives Lab 5)

This is where you define the fields that appear on the screen (application) the barista
sees and tell WMP how this application (user interface) fits into the overall workflow.

Note:  the comments here assume you have already read through the comments
in CoffeeBackend.py and OrderTakerApplication.py and made your edits there.
'''

from frontend.roleApplication import RoleApplication
from frontend.form import Type
from StoreConstants import theflowname

class WarehouseApplication(RoleApplication):
    '''
    The BaristaApplication "class" is a collection of the "methods" (functions) that 
    define the elements of the order taker application.  
    
    An application will always include the method __init__ and at least one
    method to define a form that the user of this application will use.
    '''

    def __init__(self):
        '''
        Declare this application to be part of a given work flow and specify its role in that workflow.
        '''
        # Declare this application to be part of a given workflow, and responsible for a given role:
        super(WarehouseApplication, self).__init__(theflowname, "Warehouse") 
        
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual task name and name_fields:
        self.register_sink_step("Processing", self.prepare_drink_form_creator, name_fields=['Wood', 'Glue','Saw'])
        self.register_sink_step("Processing", self.take_drink_order_form_creator) 

    def prepare_drink_form_creator(self, stepname, form):
        '''
        Defines the data entry form for the barista application.
        This form appears once the barista selects one of the pending orders from a list. NEW
        '''
        # !!! Use one or more fields from order to define label...
        form.add_task_label(fields=['Wood', 'Glue', 'Saw']) 
        # !!! Add any static labels or fields you want to include in this form...
    
    def take_drink_order_form_creator(self, stepname, form):
        '''
        This method does the actual work of building the user interface. Update 
        '''
        # !!! improve this text...
        form.add_field(Type.INTEGER, "Wood")
        form.add_field(Type.INTEGER, "Glue")
        form.add_field(Type.INTEGER, "Saw")

if __name__ == '__main__':
    #starts up the BaristaApplication:
    app = WarehouseApplication()
    #Start interacting with the user:
    app.MainLoop()
