<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema">
<xsl:template match="/">
  <html>
  <body style="font-family: Arial">

<!-- Test set (folder) summary -->
          <table border="1" cellpadding="5" align="center">
          <tr>
                    <th>Name</th>
                    <th>Tests</th>
                    <th>Passed</th>
                    <th>Failed</th>
                    <th>Skipped</th>
                    <th>Errors</th>
          </tr>
     <xsl:for-each select="testsuite/testset">
          <tr>
	     <td> <xsl:value-of select="properties/property/@value" /> </td>
	     <td> <xsl:value-of select="@tests" /> </td>
	     <td style="color: green"> <xsl:value-of select="@passes" /> </td>
	     <td style="color: red"> <xsl:value-of select="@failures" /> </td>
	     <td> <xsl:value-of select="@skips" /> </td>
	     <td style="color: red"> <xsl:value-of select="@errors" /> </td>
          </tr>

     

    </xsl:for-each>
    <xsl:for-each select="testsuite">
    <tr  style="font-weight:bold">
       <td> Totals </td>
       <td> <xsl:value-of select="@tests" /> </td>
       <td style="color: green"> <xsl:value-of select="@passes" /> </td>
       <td style="color: red"> <xsl:value-of select="@failures" /> </td>
       <td> <xsl:value-of select="@skips" /> </td>
       <td style="color: red"> <xsl:value-of select="@errors" /> </td>
    </tr>
    </xsl:for-each>

   </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet> 
