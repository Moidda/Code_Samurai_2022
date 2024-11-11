# Live Demonstration
[Youtube](https://www.youtube.com/watch?v=Edxe6fTzqfA)

# Repository for Code Samurai 2022 Hackathon

# Schema Diagram
![image](https://github.com/Moidda/Code_Samurai_2022/assets/57999057/0755f3c1-b7a2-410b-80ac-605819693f8f)


# Loading into database when server starts
```python
from django.db import connection

class MyAppConfig(AppConfig):
    default_auto_field = '...'
    name = 'MyApp'

    def ready(self) -> None:
        from .models import MyApp

        all_tables = connection.introspection.table_names()
        if 'MyApp_myApp' not in all_tables:
            return
        # code here
```

# List of csv files
- agencies
    - code
    - name
    - type
    - description

- components
    - project_id
    - executing_agency
    - component_id
    - component_type

- constraints
    - latitude
    - longitude
    - max_projects

- projects
    - name
    - location
    - latitude
    - longitude
    - exec
    - cost
    - timespan
    - project_id
    - goal
    - start_date
    - completion
    - actual_cost

- proposals
    - name
    - location
    - latitude
    - longitude
    - exec
    - cost
    - timespan
    - project_id
    - goal
    - proposal_date

- user_types
    - code
    - committee
    - description
