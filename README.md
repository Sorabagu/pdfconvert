<h1>PDFConvert</h1>
<h2>Français</h2>
<ul>
<li><h3>Description</h3>
PDFConvert est un script Python développé par Soradev qui permet de convertir des fichiers EML (ou HTML) en PDF. Il utilise l'exécutable wkhtmltopdf pour effectuer la conversion tout en gérant les erreurs courantes qui pourraient survenir pendant le processus.
<br></li>
<li><h3>Fonctionnalités</h3>
<ul>
    <li>Conversion de contenu HTML en fichiers PDF.</li>
    <li>Gestion des erreurs communes liées à wkhtmltopdf.</li>
    <li>Génération de fichiers PDF uniques en cas de conflit de noms.</li>
</ul></li>
<li><h3>Prérequis</h3>
Assurez-vous que wkhtmltopdf est correctement installé dans le répertoire bin/wkhtmltox/bin/ de l'application.
<ul>
    <li>Créez un dossier nommé <strong>wkhtmltopdf</strong> dans le répertoire du script.</li>
    <li>Téléchargez <strong>wkhtmltopdf</strong> depuis cette page internet : <a href="https://wkhtmltopdf.org/downloads.html">https://wkhtmltopdf.org/downloads.html</a>.</li>
    <li>Installez <strong>wkhtmltopdf</strong> dans le répertoire <strong>wkhtmltopdf</strong> que vous avez créé.</li>
</ul></li>
<li><h3>Utilisation</h3>
Pour utiliser le script, appelez la fonction convert_html_to_pdf(html_content, output_pdf_file) avec le contenu HTML à convertir et le chemin de sortie pour le fichier PDF.</li>
<br>
<h2>English</h2>
<li><h3>Description</h3>
PDFConvert is a Python script developed by Soradev that converts HTML files to PDF. It uses the wkhtmltopdf executable to perform the conversion while handling common errors that might occur during the process.
<br></li>
<li><h3>Features</h3>
<ul>
    <li>Converts HTML content to PDF files.</li>
    <li>Handles common wkhtmltopdf related errors.</li>
    <li>Generates unique PDF files in case of filename conflicts.</li>
</ul></li>
<li><h3>Requirements</h3>
Ensure that wkhtmltopdf is properly installed in the application's bin/wkhtmltox/bin/ directory.
<ul>
    <li>Create a folder named <strong>wkhtmltopdf</strong> in the script's directory.</li>
    <li>Download <strong>wkhtmltopdf</strong> from this webpage: <a href="https://wkhtmltopdf.org/downloads.html">https://wkhtmltopdf.org/downloads.html</a>.</li>
    <li>Install <strong>wkhtmltopdf</strong> in the <strong>wkhtmltopdf</strong> directory you just created.</li>
</ul></li>
<li><h3>Usage</h3>
To use the script, call the function convert_html_to_pdf(html_content, output_pdf_file) with the HTML content to be converted and the output path for the PDF file.</li>
</ul>
