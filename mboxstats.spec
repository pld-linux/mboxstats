Summary:	Several top-10 lists from messages in mbox format
Summary(pl.UTF-8):	Tworzenie list dziesięciu najlepszych z wiadomości w formacie mbox
Name:		mboxstats
Version:	2.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/mboxstats/%{name}-%{version}.tgz
# Source0-md5:	527c73a6adaa90a1e928f65342fa8da4
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

%description -l pl.UTF-8
mboxstats tworzy różne listy dziesięciu najlepszych ("top-10") z pliku
zawierającego wiadomości w formacie mbox. Oto lista możliwych do
uzyskania list:
 - najwięcej piszących
 - najwięcej otrzymujących
 - najpopularniejszych tematów
 - najwięcej otrzymujących jako kopię (cc)
 - najczęściej spotykanych domen najwyższego poziomu (TLD)
 - najczęściej spotykanych stref czasowych
 - najczęściej spotykanych organizacji
 - najczęściej używanych programów pocztowych
 - najpopularniejszego czasu wysyłania (miesięcy, dni miesiąca,
   dni tygodnia, godzin)
 - średniej liczby linii w wiadomości
 - wszystkich rodzajów statystyk dla użytkownika
 - wiele więcej!

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
