# **CSV TO PDF CONVERTER ( .csv ➜ .pdf )**

## ***A Python module that allows you to convert CSV FILES to PDF FILES easily!***

![](https://raw.githubusercontent.com/TECH-SAVVY-GUY/csv2pdf/master/convert.png)

### Installation

```python
pip install csv2pdf
```


### Examples 📋

```python
# Quick conversion

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf")
```

```python
# Change Orientation of the PDF File

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf", orientation="L")
```

```python
# Specify Delimiter for the CSV File

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf", delimiter="&")
```

```python
# Change Alignment of the cells

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf", align="L")

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf", align="R")
```

```python
# Change Size & Header-Size

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf", size=5)

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf", headersize=7)
```

```python
# Using custom fonts

>>> from csv2pdf import convert
>>> convert("source.csv", "destination.pdf",
            font=r"Fonts\custom-font.tff", headerfont=r"Fonts\custom-header-font.tff")
```

***Use*** `.tff` ***files for specifying font files. Fonts can be downloaded from **[Google Fonts](https://fonts.google.com/)**.***
