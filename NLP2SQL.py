import os
import openai
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY');
openai.api_key = api_key

import panel as pn


def continue_conversation(messages, temperature =0): 
        response = openai.ChatCompletion.create(
                model="gpt-4", 
                messages=messages, 
                temperature=temperature)
        return response.choices[0].message["content"]


context = [ {'role':'system', 'content':"""
you are a bot to assist in create SQL commands, all your answers should start with \
this is your SQL, and after that an SQL that can do what the user request. \
Your Database is composed by a SQL database with some tables. \
Try to Maintain the SQL order simple.
Put the SQL command in white letters with a black background, and just after \
a simple and concise text explaining how it works. 
If the user ask for something that can not be solved with an SQL Order \
just answer something nice and simple and ask him for something that \
can be solved with SQL. 
"""} ]


context.append( {'role':'system', 'content':"""
first table: 
{
  "tableName": "employees",
  "fields": [
    {
      "nombre": "ID_usr",
      "tipo": "int"
    },
    {
      "nombre": "name",
      "tipo": "string"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
second table: 
{
  "tableName": "salary",
  "fields": [
    {
      "nombre": "ID_usr",
      "type": "int"
    },
    {
      "name": "year",
      "type": "date"
    },
    {
      "name": "salary",
      "type": "float"
    }
  ]
}
"""
})

context.append( {'role':'system', 'content':"""
third table: 
{
  "tablename": "studies",
  "fields": [
    {
      "name": "ID",
      "type": "int"
    },
    {
      "name": "ID_usr",
      "type": "int"
    },
    {
      "name": "educational level",
      "type": "int"
    },
    {
      "name": "Institution",
      "type": "string"
    },
    {
      "name": "Years",
      "type": "date"
    }
    {
      "name": "Speciality",
      "type": "string"
    }
  ]
}
"""
})


def add_prompts_conversation(_):
    #Get the value introduced by the user
    prompt = client_prompt.value_input
    client_prompt.value = ''
    
    #Append to the context the User promnopt. 
    context.append({'role':'user', 'content':f"{prompt}."})
    context.append({'role':'system', 'content':f"Remember your instructions as SQL Assistant."})
    
    #Get the response. 
    response = continue_conversation(context) 
    
    #Add the response to the context. 
    context.append({'role':'assistant', 'content':f"{response}"})
    
    #Undate the panels to shjow the conversation. 
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

pn.extension()

panels = [] 

client_prompt = pn.widgets.TextInput(value="Hi", placeholder='Order your data…')
button_conversation = pn.widgets.Button(name="generate SQL")

interactive_conversation = pn.bind(add_prompts_conversation, button_conversation)

dashboard = pn.Column(
    client_prompt,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard.show()

