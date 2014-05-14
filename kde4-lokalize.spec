#
# TODO:
# - add man files
#
%define		orgname		lokalize
%define		_state		stable
%define		qtver		4.8.1

Summary:	Computer-aided translation system that focuses on productivity and performance
Name:		kde4-%{orgname}
Version:	4.13.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7908954a354c434d8a10fe9403a289d0
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	hunspell-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdesdk-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lokalize is a computer-aided translation system that focuses on
productivity and performance. Translator does only creative work (of
delivering message in his/her mother language in laconic and easy to
understand form). Lokalize implies parapgraph-by-paragrah translation
approach (when translating documentation) and message-by-message
approach (when translating GUI).

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	%{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lokalize
%{_datadir}/apps/lokalize
%{_datadir}/config.kcfg/lokalize.kcfg
#%{_datadir}/config.kcfg/pocreatorsettings.kcfg
#%{_datadir}/kde4/services/pothumbnail.desktop
%{_desktopdir}/kde4/lokalize.desktop
#%{_iconsdir}/*/*/actions/msgid2msgstr.png
#%{_iconsdir}/*/*/actions/insert_arg.png
#%{_iconsdir}/*/*/actions/prevfuzzy.png
#%{_iconsdir}/*/*/actions/insert_tag.png
#%{_iconsdir}/*/*/actions/approved.png
#%{_iconsdir}/*/*/actions/diff.png
#%{_iconsdir}/*/*/actions/preverror.png
#%{_iconsdir}/*/*/actions/prevfuzzyuntrans.png
#%{_iconsdir}/*/*/actions/prevpo.png
#%{_iconsdir}/*/*/actions/prevtemplate.png
#%{_iconsdir}/*/*/actions/search2msgstr.png
%{_iconsdir}/*/*/apps/lokalize.png
#%{_iconsdir}/*/*/actions/nexterror.png
#%{_iconsdir}/*/*/actions/nextfuzzy.png
#%{_iconsdir}/*/*/actions/nextfuzzyuntrans.png
#%{_iconsdir}/*/*/actions/nextpo.png
#%{_iconsdir}/*/*/actions/nexttemplate.png
#%{_iconsdir}/*/*/actions/nextuntranslated.png
#%{_iconsdir}/*/*/actions/prevuntranslated.png
#%{_iconsdir}/*/*/actions/transsearch.png
#%{_iconsdir}/*/*/actions/catalogmanager.png
#%{_iconsdir}/*/*/actions/approved.svgz
%{_iconsdir}/*/*/apps/lokalize.svgz
