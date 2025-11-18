<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
  xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
  exclude-result-prefixes="table text">

  <xsl:param name="sheet_name"/>

  <xsl:template match="/">
    <xsl:apply-templates select="//table:table[@table:name=$sheet_name]"/>
  </xsl:template>

  <xsl:template match="table:table">
    <table>
      <xsl:apply-templates select="table:table-row[1]" mode="header"/>
      <xsl:apply-templates select="table:table-row[position()>1 and not(@table:number-rows-repeated)]" mode="body"/>
    </table>
  </xsl:template>

  <!-- Capçalera -->
  <xsl:template match="table:table-row" mode="header">
    <tr>
      <xsl:apply-templates select="table:table-cell | table:covered-table-cell" mode="header"/>
    </tr>
  </xsl:template>

  <xsl:template match="table:table-cell" mode="header">
    <xsl:call-template name="render-cell">
      <xsl:with-param name="tag" select="'th'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="table:covered-table-cell" mode="header">
    <th></th>
  </xsl:template>

  <!-- Cos de taula -->
  <xsl:template match="table:table-row" mode="body">
    <xsl:if test="table:table-cell[text:p[normalize-space()]]">
      <tr>
        <xsl:apply-templates select="table:table-cell | table:covered-table-cell" mode="body"/>
      </tr>
    </xsl:if>
  </xsl:template>

  <xsl:template match="table:table-cell" mode="body">
    <xsl:call-template name="render-cell">
      <xsl:with-param name="tag" select="'td'"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="table:covered-table-cell" mode="body">
    <!-- No generem res: cel·la ja està coberta -->
  </xsl:template>

  <!-- Cel·la -->
  <xsl:template name="render-cell">
    <xsl:param name="tag" select="'td'"/>
    <xsl:variable name="repeat" select="number(@table:number-columns-repeated)" />
    <xsl:variable name="colspan" select="@table:number-columns-spanned" />
    <xsl:variable name="rowspan" select="@table:number-rows-spanned" />
    <xsl:variable name="value">
      <xsl:apply-templates select="text:p"/>
    </xsl:variable>

    <xsl:choose>
      <xsl:when test="$repeat &gt; 1">
        <xsl:call-template name="repeat-cell">
          <xsl:with-param name="tag" select="$tag"/>
          <xsl:with-param name="value" select="$value"/>
          <xsl:with-param name="count" select="$repeat"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:element name="{$tag}">
          <xsl:if test="$colspan">
            <xsl:attribute name="colspan">
              <xsl:value-of select="$colspan"/>
            </xsl:attribute>
          </xsl:if>
          <xsl:if test="$rowspan">
            <xsl:attribute name="rowspan">
              <xsl:value-of select="$rowspan"/>
            </xsl:attribute>
          </xsl:if>
          <xsl:copy-of select="$value"/>
        </xsl:element>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- Repetició de cel·les -->
  <xsl:template name="repeat-cell">
    <xsl:param name="tag"/>
    <xsl:param name="value"/>
    <xsl:param name="count"/>
    <xsl:if test="$count &gt; 0">
      <xsl:element name="{$tag}">
        <xsl:copy-of select="$value"/>
      </xsl:element>
      <xsl:call-template name="repeat-cell">
        <xsl:with-param name="tag" select="$tag"/>
        <xsl:with-param name="value" select="$value"/>
        <xsl:with-param name="count" select="$count - 1"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>

  <!-- Text -->
  <xsl:template match="text:p">
    <xsl:value-of select="."/>
    <xsl:if test="position() != last()">
      <br/>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>