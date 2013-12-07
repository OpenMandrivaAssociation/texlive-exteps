# revision 19859
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/exteps
# catalog-date 2007-03-06 10:34:25 +0100
# catalog-license gpl
# catalog-version 0.41
Name:		texlive-exteps
Version:	0.41
Release:	6
Summary:	Include EPS figures in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/exteps
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.41-2
+ Revision: 751738
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.41-1
+ Revision: 718404
- texlive-exteps
- texlive-exteps
- texlive-exteps
- texlive-exteps

