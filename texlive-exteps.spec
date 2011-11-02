Name:		texlive-exteps
Version:	0.41
Release:	1
Summary:	Include EPS figures in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/exteps
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Exteps is a module for including external EPS figures into
MetaPost figures. It is written entirely in MetaPost, and does
not therefore require any post processing of the MetaPost
output.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
