# Read name and marks from file
with open("student.txt", "r") as f:
    name = f.readline().strip()
    marks = [int(f.readline()) for _ in range(3)]

# Calculate average and grade
average = sum(marks) / 3
grade = 'A' if average >= 80 else 'B' if average >= 60 else 'C'

# Generate HTML with table
with open("report.html", "w") as f:
    f.write(f"""
    <html>
    <head>
        <title>Report Card</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            h2 {{
                color: #333;
            }}
            table {{
                width: 60%;
                border-collapse: collapse;
                margin-top: 20px;
                background-color: #fff;
            }}
            th, td {{
                padding: 10px;
                border: 1px solid #ccc;
                text-align: center;
            }}
            th {{
                background-color: #eee;
            }}
        </style>
    </head>
    <body>
        <h2>Student Report Card</h2>
        <p><b>Name:</b> {name}</p>
        <table>
            <tr>
                <th>Subject 1</th>
                <th>Subject 2</th>
                <th>Subject 3</th>
                <th>Average</th>
                <th>Grade</th>
            </tr>
            <tr>
                <td>{marks[0]}</td>
                <td>{marks[1]}</td>
                <td>{marks[2]}</td>
                <td>{average:.2f}</td>
                <td>{grade}</td>
            </tr>
        </table>
    </body>
    </html>
    """)
print("✅ Report generated successfully as report.html")
