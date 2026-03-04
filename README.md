# APORIA

## Overview
Most people don't realize their own logical inconsistencies until they see them. Aporia provides that visual "aha!" moment.  
It is a conversational mirror for your thoughts. It uses Gemini Live API to map out your arguments as you speak, helping you identify contradictions and refine your reasoning through the Socratic method.

## Project Structure
```
APORIA/
├── app/
│   ├── __init__.py
│   ├── main.py              
│   ├── api/                 
│   │   ├── __init__.py
│   │   ├── deps.py          
│   │   └── v1/
│   │       ├── api.py       
│   │       └── endpoints/
│   │           └── dialectic.py 
│   ├── core/                
│   │   ├── __init__.py
│   │   └── config.py        
│   ├── services/            
│   │   ├── __init__.py
│   │   ├── philosopher.py   
│   │   └── cartographer.py  
│   ├── schemas/             
│   │   └── graph.py         
│   └── static/              
│       ├── index.html       
│       ├── debate.html      
│       ├── css/             
│       └── js/             
├── .env                     
├── requirements.txt
└── Dockerfile             
```
