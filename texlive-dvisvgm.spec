# revision 26885
# category TLCore
# catalog-ctan /dviware/dvisvgm
# catalog-date 2011-12-20 12:24:43 +0100
# catalog-license gpl
# catalog-version 1.0.10
Name:		texlive-dvisvgm
Version:	1.0.10
Release:	1
Summary:	Converts DVI files to Scalable Vector Graphics format (SVG)
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
to the XML-based Scalable Vector Graphics format. The current
version provides basic conversion functionality; development of
an improved version continues. Users will need a working TeX
installation including the kpathsea library and Type 1 versions
of the fonts used in the DVI file. Dvisvgm has been
successfully tested .

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/dvisvgm.1*
%doc %{_texmfdir}/doc/man/man1/dvisvgm.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
