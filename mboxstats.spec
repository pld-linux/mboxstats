Summary:	Creates several top-10 lists from messages in mbox format
Summary(pl):	Tworzy listy dziesiêciu najlepszych z wiadomo¶ci w formacie mbox
Name:		mboxstats
Version:	1.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/mboxstats/%{name}-%{version}.tgz
# Source0-md5:	14e4b1cba0b778dff00db8eb10b9291c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mboxstats creates several top-10 lists from a file containing message
in mbox-format. List of top10 lists:

    - Top writes
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

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcflags}" \
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
