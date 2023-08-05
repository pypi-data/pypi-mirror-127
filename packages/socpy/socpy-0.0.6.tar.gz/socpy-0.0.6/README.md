# socpy
Query the [SOCcer API](https://soccer.nci.nih.gov/soccer/) 
with Python.

## Description
This package provides an interface to query the SOCcer API.
The functionality is vectorized and returns responses in a
structured manner (pandas dataframes).

## Installation
Install from [PyPI](https://pypi.org/) with pip:
```
pip install socpy
```

## Example
This is a basic example of how to use the package:


```python
import socpy
```

Using the built-in data set we can query the first three jobs and view the results. The first three job postings:


```python
job_desc = socpy.load_jobs()
job_desc.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>job_id</th>
      <th>title</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>140906257</td>
      <td>deli clerk customer service</td>
      <td>polite prompt knowledgeable|preparing order pa...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>140974158</td>
      <td>roll off truck driver class b cdl 3 000 bonus</td>
      <td>operate manual automatic control accordance sa...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>140923731</td>
      <td>field engineer 3</td>
      <td>perform advanced troubleshooting repair assign...</td>
    </tr>
  </tbody>
</table>
</div>



Now, using socpy to return the top three SOC matches for each:


```python
jobs = socpy.soccer(
    job_title = list(job_desc.loc[0:2, 'title']),
    job_desc = list(job_desc.loc[0:2, 'description']),
    n_results = 3,
    job_id = list(job_desc.loc[0:2, 'job_id'])
)
```

The `jobs` object has two methods; namely, `jobs.problems` which contains any API requests that encountered issues, and `jobs.valid` which contains the output from all valid API requests. First, we can ensure that no problems were encountered when querying the API:


```python
jobs.problems == None
```




    True



Next, we can view the top three results for each of our three job descriptions.


```python
jobs.valid
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>code</th>
      <th>label</th>
      <th>score</th>
      <th>job_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>43-4051</td>
      <td>Customer Service Representatives</td>
      <td>0.202345</td>
      <td>140906257</td>
    </tr>
    <tr>
      <th>1</th>
      <td>35-2021</td>
      <td>Food Preparation Workers</td>
      <td>0.107131</td>
      <td>140906257</td>
    </tr>
    <tr>
      <th>2</th>
      <td>35-3021</td>
      <td>Combined Food Preparation and Serving Workers,...</td>
      <td>0.060109</td>
      <td>140906257</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53-3032</td>
      <td>Heavy and Tractor-Trailer Truck Drivers</td>
      <td>0.969044</td>
      <td>140974158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>53-3011</td>
      <td>Ambulance Drivers and Attendants, Except Emerg...</td>
      <td>0.003048</td>
      <td>140974158</td>
    </tr>
    <tr>
      <th>5</th>
      <td>55-3014</td>
      <td>Artillery and Missile Crew Members</td>
      <td>0.001014</td>
      <td>140974158</td>
    </tr>
    <tr>
      <th>6</th>
      <td>43-9061</td>
      <td>Office Clerks, General</td>
      <td>0.019577</td>
      <td>140923731</td>
    </tr>
    <tr>
      <th>7</th>
      <td>17-2112</td>
      <td>Industrial Engineers</td>
      <td>0.005500</td>
      <td>140923731</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17-2171</td>
      <td>Petroleum Engineers</td>
      <td>0.005500</td>
      <td>140923731</td>
    </tr>
  </tbody>
</table>
</div>
