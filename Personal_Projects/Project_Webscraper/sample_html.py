import webbrowser

sample_html_template = """
<!DOCTYPE html>
<html lang='en'>
    <head> Average number of push-ups completed per continent </head>
<body>
    <div class={div_class} id={div_class_id}>
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
        </table>
    </div>
    <div class={fodder_div_class} id={fodder_div_class_id}>
        <p> Random non-statistics information irrelevant to the aim of the webscraper.</p>
        <p> This is just here to see if the webscraper is <span style="color: blue;">correctly</span> applied to the content we want to retrieve.</p>
    </div>
</body>
"""

DIV_CLASS = 'Fabricated_statistics'
DIV_CLASS_ID = 'Demographic stats'
FODDER_DIV_CLASS = 'Irrelevant_information'
FODDER_DIV_CLASS_ID = 'Text containing information we are not interested in'

html_page_information = sample_html_template.format(
    div_class=DIV_CLASS,
    div_class_id=DIV_CLASS_ID,
    fodder_div_class=FODDER_DIV_CLASS,
    fodder_div_class_id=FODDER_DIV_CLASS_ID,
)


def write_to_html_file(html_template: str) -> str:
    sample_page = 'sample_page.html'
    with open(sample_page, 'w') as file:
        file.write(html_template)
    return sample_page


write_to_html_file(html_page_information)

# Open html file on a browser
webbrowser.open('sample_page.html')