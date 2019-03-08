def test():
    import pdfkit
    body = """
        <html>
          <head>
            <meta name="pdfkit-page-size" content="Legal"/>
            <meta name="pdfkit-orientation" content="Landscape"/>
          </head>
          Hello World!
          </html>
        """
    pdfkit.from_string(body, '/opt/edx-hawthorn.2-4/apps/edx/edx-platform/testpdf/out.pdf')  # with --page-size=Legal and --orientation=Landscape
