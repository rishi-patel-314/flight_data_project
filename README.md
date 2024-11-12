# flight_data_project
Python program that accomplishes both phases: 
the generation of random flight data and its subsequent analysis and cleaning.
The program is designed to run locally and leverages efficient libraries like pandas
for data manipulation. It handles the tasks of generating JSON files, 
analyzing flight records, and calculating the requested statistics


flight_data_project/
├── /tmp/flights/               # Directory for generated flight JSON files (handled by the system)
├── scripts/
│   ├── generate_data.py        # Script for data generation phase
│   ├── analyze_data.py         # Script for analysis and cleaning phase
├── utils/
│   ├── file_utils.py           # Utility functions for file handling
│   └── data_utils.py           # Utility functions for data manipulation
├── constants/
│   └── config.py               # Configuration constants
├── tests/
│   ├── test_generate_data.py   # Unit tests for data generation
│   ├── test_analyze_data.py    # Unit tests for data analysis
│   ├── test_file_utils.py      # Unit tests for file utilities
│   └── test_data_utils.py      # Unit tests for data utilities
├── requirements.txt            # File listing Python dependencies
└── README.md                   # Project description and instructions
