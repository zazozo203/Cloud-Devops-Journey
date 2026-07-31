

try:
        import csv
        from pathlib import Path
        file_path = Path("/mnt/c/Users/zazozo/desktop/practice/list.csv")
        file_path.touch(exist_ok=True)
        
        def Read_Csv():

            if file_path.is_file():
                with open(file_path, 'r', encoding='utf-8') as f:
                      reader = csv.DictReader(f)
                      return list(reader)

        def Analyse_Csv(tasks):
             
                frequency = {}
                Total= 0
                count_valid = 0
                for read in tasks:
                    cleaned_row = {k.strip(): v.strip() for k, v in read.items()}
                    cat = cleaned_row['category']
                    frequency[cat] =frequency.get(cat, 0) + 1
                    try:
                            amount = float(read['amount'])
                            Total = Total + amount
                            count_valid +=1
                    except ValueError as e:
                                      print(e)
                                      continue
                            
                return frequency,Total,count_valid
             
                        

        content = Read_Csv()
        if len(content) == 0:
              print("file is empty")
        else:
              print(content)
        freq,Tot,valid = Analyse_Csv(content)
        print(freq)
        print(f'The total amount = {Tot} for a valid count of {valid} for the total {len(content) } available')
              
except Exception as e:
         print(e)

  