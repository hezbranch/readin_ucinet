# readin_ucinet
Read in UCINET text files as pandas DataFrame

Available at: https://pypi.org/project/readin-ucinet/

**Prerequisites:** Requires pandas installation <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html?highlight=install

**Example Usage:** <br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; import readin_ucinet as ru <br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; social_graph = ru.read_ucinet("ENTER_FILEPATH_HERE")

**Returns: pandas DataFrame or TextParser <br/>**
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.

