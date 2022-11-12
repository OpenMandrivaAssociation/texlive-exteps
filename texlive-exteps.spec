Name:		texlive-exteps
Version:	19859
Release:	1
Summary:	Include EPS figures in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/exteps
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Exteps is a module for including external EPS figures into
MetaPost figures. It is written entirely in MetaPost, and does
not therefore require any post processing of the MetaPost
output.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/exteps/exteps.mp
%doc %{_texmfdistdir}/doc/metapost/exteps/LICENSE
%doc %{_texmfdistdir}/doc/metapost/exteps/README
%doc %{_texmfdistdir}/doc/metapost/exteps/delfin
%doc %{_texmfdistdir}/doc/metapost/exteps/exteps.pdf
%doc %{_texmfdistdir}/doc/metapost/exteps/exteps.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
