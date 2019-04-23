#
# TODO:
# - add man files
#
%define		orgname		lokalize
%define		_state		stable
%define		qtver		4.8.1

Summary:	Computer-aided translation system that focuses on productivity and performance
Summary(pl.UTF-8):	System komputerowo wspomaganego tłumaczenia skupiający się na produktywności i wydajności
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	4
License:	GPL v2 or GPL v3
Group:		X11/Development/Tools
Source0:	https://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b83fa21c233a60605eea717c20b84dfb
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	hunspell-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info
BuildRequires:	utempter-devel
Obsoletes:	kde4-kdesdk-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lokalize is a computer-aided translation system that focuses on
productivity and performance. Translator does only creative work (of
delivering message in his/her mother language in laconic and easy to
understand form). Lokalize implies paragraph-by-paragraph translation
approach (when translating documentation) and message-by-message
approach (when translating GUI).

%description -l pl.UTF-8
Lokalize to system komputerowo wspomaganego tłumaczenia, skupiający
się na produktywności i wydajności. Tłumacz wykonuje tylko pracę
twórczą (dostarczania komunikatów w języku ojczystym w zwięzłej i
łatwo zrozumiałej postaci). Lokalize zakłada podejście tłumaczenia
"akapit po akapicie" (przy tłumaczeniu dokumentacji) oraz "komunikat
po komunikacie" (przy tłumaczeniu interfejsów graficznych).

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lokalize
%{_datadir}/apps/lokalize
%{_datadir}/config.kcfg/lokalize.kcfg
%{_desktopdir}/kde4/lokalize.desktop
%{_iconsdir}/hicolor/*x*/apps/lokalize.png
%{_iconsdir}/hicolor/scalable/apps/lokalize.svgz
