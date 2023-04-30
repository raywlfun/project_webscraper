import webbrowser

sample_html_template = """
<!DOCTYPE html>
<html lang='en' class={div_class_label} id={div_class_id}>
    <head> Average number of push-ups completed per continent </head>
    <p>Here, we report <span style="color: red;">fabricated</span> data pertaining to the average number of pushups completed within a household, from 2021 - 2022 - amongst the following continents:</p>
    <ul>
        <li>Asia</li>
        <li>Africa</li>
        <li>Europe</li>
        <li>North America</li>
        <li>South America</li>
        <li>Australia</li>
        <li>Antarctica</li>
    </ul>
    <table>
        <thead>
            <tr>
                <th>Country</th>
                <th>Totally accurate demographic</th>
                <th>Avg. Push-ups</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Asia</td>
                <td>4,694,576,167</td>
                <td>2,500,000,000</td>
            </tr>
            <tr>
                <td>Africa</td>
                <td>1,393,676,444</td>
                <td>1,000,000,000</td>
            </tr>
            <tr>
                <td>Europe</td>
                <td>745,173,774</td>
                <td>500,000,000</td>
            </tr>
            <tr>
                <td>North America</td>
                <td>595,783,465</td>
                <td>400,000,000</td>
            </tr>
            <tr>
                <td>South America</td>
                <td>434,254,119</td>
                <td>275,000,000</td>
            </tr>
            <tr>
                <td>Australia / Oceania</td>
                <td>44,491,724</td>
                <td>20,000,000</td>
            </tr>
            <tr>
                <td>Antarctica</td>
                <td>3,000</td>
                <td>1,200</td>
            </tr>
"""

div_class_label = 'Sample statistical data pertaining to made-up demographics'
div_class_id = 'Demographic stats'

html_page = sample_html_template.format(div_class_label=div_class_label, div_class_id=div_class_id)

with open('sample_page.html', 'w') as file:
    file.write(html_page)

# Open html file on a browser
webbrowser.open('sample_page.html')