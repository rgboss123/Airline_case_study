{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3b5ecf57-f148-4454-9973-3c1aa126d20a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "⬆ Loading Aircraft_costs.csv → table `aircraft_costs`\n",
      "⬆ Loading Aircraft_Maintenance.csv → table `aircraft_maintenance`\n",
      "⬆ Loading Baggage_Details.csv → table `baggage_details`\n",
      "⬆ Loading Crew_Assignments.csv → table `crew_assignments`\n",
      "⬆ Loading Customer_Feedback.csv → table `customer_feedback`\n",
      "⬆ Loading Flights.csv → table `flights`\n",
      "⬆ Loading Flight_Delays.csv → table `flight_delays`\n",
      "⬆ Loading Passengers.csv → table `passengers`\n",
      "⬆ Loading Passport_Details.csv → table `passport_details`\n",
      "⬆ Loading Revenue_Transactions.csv → table `revenue_transactions`\n",
      "⬆ Loading Visa_Details.csv → table `visa_details`\n",
      "✅ All CSV files loaded into PostgreSQL successfully\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# ---------- DB CONFIG ----------\n",
    "DB_HOST = \"localhost\"\n",
    "DB_PORT = \"5432\"\n",
    "DB_NAME = \"Airline_data\"\n",
    "DB_USER = \"postgres\"\n",
    "DB_PASSWORD = \"*Ritwik1\"\n",
    "\n",
    "# ---------- CSV FOLDER ----------\n",
    "FOLDER_PATH = r\"C:\\Users\\user\\Downloads\\airline_data_processed\"\n",
    "\n",
    "# ---------- CREATE ENGINE ----------\n",
    "engine = create_engine(\n",
    "    f\"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}\"\n",
    ")\n",
    "\n",
    "# ---------- LOAD CSV FILES ----------\n",
    "for file in os.listdir(FOLDER_PATH):\n",
    "    if file.lower().endswith(\".csv\"):\n",
    "        table_name = file.replace(\".csv\", \"\").lower()\n",
    "        file_path = os.path.join(FOLDER_PATH, file)\n",
    "\n",
    "        print(f\"⬆ Loading {file} → table `{table_name}`\")\n",
    "\n",
    "        df = pd.read_csv(file_path)\n",
    "\n",
    "        df.to_sql(\n",
    "            table_name,\n",
    "            engine,\n",
    "            if_exists=\"replace\",   # use \"append\" if needed\n",
    "            index=False,\n",
    "            chunksize=20000,       # VERY important for RAM\n",
    "            method=\"multi\"\n",
    "        )\n",
    "\n",
    "print(\"✅ All CSV files loaded into PostgreSQL successfully\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e6e71e26-e79c-4949-9b21-341f1bfeb051",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting psycopg2\n",
      "  Downloading psycopg2-2.9.11-cp312-cp312-win_amd64.whl.metadata (5.1 kB)\n",
      "Downloading psycopg2-2.9.11-cp312-cp312-win_amd64.whl (2.7 MB)\n",
      "   ---------------------------------------- 0.0/2.7 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/2.7 MB ? eta -:--:--\n",
      "   ----------- ---------------------------- 0.8/2.7 MB 2.6 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 2.1/2.7 MB 4.5 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 2.7/2.7 MB 4.8 MB/s eta 0:00:00\n",
      "Installing collected packages: psycopg2\n",
      "Successfully installed psycopg2-2.9.11\n"
     ]
    }
   ],
   "source": [
    "!pip install psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7cce1d91-3a8d-4914-98d2-e129c51fba25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Loaded files: ['Aircraft_costs', 'Aircraft_Maintenance', 'Baggage_Details', 'Crew_Assignments', 'Customer_Feedback', 'Flights', 'Flight_Delays', 'Passengers', 'Passport_Details', 'Revenue_Transactions', 'Visa_Details']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "folder_path = r\"C:\\Users\\user\\Downloads\\airline_data_processed\"   # 🔁 change this to your folder path\n",
    "\n",
    "dataframes = {}\n",
    "\n",
    "for file in os.listdir(folder_path):\n",
    "    if file.endswith(\".csv\"):\n",
    "        file_path = os.path.join(folder_path, file)\n",
    "        df_name = file.replace(\".csv\", \"\")\n",
    "        dataframes[df_name] = pd.read_csv(file_path)\n",
    "\n",
    "print(\"✅ Loaded files:\", list(dataframes.keys()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98541448-e9b7-4c5b-aa69-61567dc9a54d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
