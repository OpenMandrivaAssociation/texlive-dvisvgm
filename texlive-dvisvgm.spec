# revision 23089
# category TLCore
# catalog-ctan /dviware/dvisvgm
# catalog-date 2011-05-18 22:35:17 +0200
# catalog-license gpl
# catalog-version 1.0.5
Name:		texlive-dvisvgm
Version:	1.0.5
Release:	1
Summary:	Converts DVI files to Scalable Vector Graphics format (SVG)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvisvgm
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvisvgm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvisvgm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-dvisvgm.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
