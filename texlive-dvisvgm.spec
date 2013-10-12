# revision 29764
# category TLCore
# catalog-ctan /dviware/dvisvgm
# catalog-date 2013-03-04 12:33:38 +0100
# catalog-license gpl
# catalog-version 1.2
Name:		texlive-dvisvgm
Version:	1.2.0
Release:	1
Summary:	Convert DVI files to Scalable Vector Graphics format (SVG)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvisvgm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvisvgm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvisvgm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dvisvgm.bin

%description
Dvisvgm is a command line utility that converts TeX DVI files
to the XML-based Scalable Vector Graphics (SVG) format. It
provides full full font support including virtual fonts, font
maps, and sub-fonts. If necessary, dvisvgm vectorizes
Metafont's bitmap output in order to always create lossless
scalable output. The embedded SVG fonts can optionally be
replaced with graphics paths so that applications that don't
support SVG fonts are enabled to render the graphics properly.
Besides many other features, dvisvgm also supports color,
emTeX, tpic, PDF mapfile and PostScript specials. Users will
need a working TeX installation including the kpathsea library.
For more detailed information, see the project page.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvisvgm.1*
%doc %{_texmfdistdir}/doc/man/man1/dvisvgm.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
