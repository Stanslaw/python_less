#!/usr/bin/env python3
import numpy as np

matrix = np.zeros((10, 10))

matrix[0, :] = list(range(1, 11))
matrix[:, 0] = list(range(1, 11))

html_head = """<html>
<body>
<table> \n"""
html_footer = """</table>
</body>
</html>"""
html_table = """"""

for row in range(matrix.shape[0]):

    html_table += """<tr> \n"""

    for col in range(matrix.shape[1]):
        html_table += """   <td>"""

        if matrix[row, col]:
            html_table += f"""<a href=http://{int(matrix[row, col])}.ru>"""
            html_table += f"""{int(matrix[row, col])}"""

        elif not matrix[row, col]:
            matrix[row, col] = matrix[0, col] * matrix[row, 0]
            html_table += f"""<a href=http://{int(matrix[row, col])}.ru>"""
            html_table += f"""{int(matrix[row, col])}"""

        html_table += f"""</a>"""

        html_table += """</td> \n"""
    html_table += """</tr> \n"""

print(html_head + html_table + html_footer)
print(matrix)