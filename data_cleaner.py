pythonimport re

def clean_customer_data(raw_data_list):
    cleaned_records = []
    
    print("Starting data cleaning process...")
    
    for record in raw_data_list:
        # Separate the messy row by commas
        parts = record.split(',')
        if len(parts) < 3:
            continue  # Skip incomplete records
            
        # 1. Clean up the Name (Strip spaces and capitalize properly)
        raw_name = parts[0]
        clean_name = raw_name.strip().title()
        
        # 2. Clean up the Email (Lowercase and remove accidental spaces)
        raw_email = parts[1]
        clean_email = raw_email.strip().lower()
        
        # 3. Clean up the Phone Number (Keep only the digits)
        raw_phone = parts[2]
        clean_phone = "".join(char for char in raw_phone if char.isdigit())
        
        # Basic validation: Add to clean records if email looks real
        if "@" in clean_email and "." in clean_email:
            formatted_record = {
                "name": clean_name,
                "email": clean_email,
                "phone": clean_phone if clean_phone else "N/A"
            }
            cleaned_records.append(formatted_record)
            print(f"Successfully cleaned record for: {clean_name}")
            
    return cleaned_records

if __name__ == "__main__":
    # Example of messy data a client might hand you from an Excel export
    messy_data = [
        "  john DOE,  JohnDoe@Gmail.com , +1-555-0192 ",
        "alice smith,ALICE@yahoo.com, 5550143",
        "invalid_row_missing_phone_and_comma"
    ]
    
    results = clean_customer_data(messy_data)
    print("\nFinal Cleaned Results:")
    for user in results:
        print(user)
