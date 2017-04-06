<!doctype html>

<table>
	<tr>
		<th>Column 1 Header</th>
		<th>Column 2 Header</th>
	</tr>
	{% for k, v in dictionary.items() %}
		<tr>
			<td>{{ k }}</td>
			<td>{{ v }}</td>
		</tr>		
	{% endfor %}
</table>
