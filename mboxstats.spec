Summary:	Several top-10 lists from messages in mbox format
Summary(pl):	Tworzenie list dziesiêciu najlepszych z wiadomo¶ci w formacie mbox
Name:		mboxstats
Version:	2.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/mboxstats/%{name}-%{version}.tgz
# Source0-md5:	7bd926282e150ea7a4fc2130040c3c96
URL:		http://www.vanheusden.com/mboxstats/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mboxstats creates several top-10 lists from a file containing message
in mbox-format. List of top10 lists:

 - Top writers
 - Top receivers
 - Top subjects
 - Top cc'ers
 - Top top-level-domain
 - Top timezones
 - Top organisations
 - Top useragents (mailprograms)
 - Top month/day-of-month/day-of-week/hour
 - Average number of lines per message
 - All kinds of per-user statistics
 - And much more!

%description -l pl
mboxstats tworzy ró¿ne listy dziesiêciu najlepszych ("top-10") z pliku
zawieraj±cego wiadomo¶ci w formacie mbox. Oto lista mo¿liwych do
uzyskania list:
 - najwiêcej pisz±cych
 - najwiêcej otrzymuj±cych
 - najpopularniejszych tematów
 - najwiêcej otrzymuj±cych jako kopiê (cc)
 - najczê¶ciej spotykanych domen najwy¿szego poziomu (TLD)
 - najczê¶ciej spotykanych stref czasowych
 - najczê¶ciej spotykanych organizacji
 - najczê¶ciej u¿ywanych programów pocztowych
 - najpopularniejszego czasu wysy³ania (miesiêcy, dni miesi±ca,
   dni tygodnia, godzin)
 - ¶redniej liczby linii w wiadomo¶ci
 - wszystkich rodzajów statystyk dla u¿ytkownika
 - wiele wiêcej!

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcflags} -DVERSION=\\\"%{version}\\\"" \
	LDFLAGS="%{rpmldflags} -lstdc++"
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mboxstats $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
