Summary:	Creates several top-10 lists from messages in mbox format
Summary(pl):	Tworzy listy dziesięciu najlepszych z wiadomości w formacie mbox
Name:		mboxstats
Version:	1.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/mboxstats/%{name}-%{version}.tgz
# Source0-md5:	5639c5f60a6259072da4d995ddd80c73
Patch0:		%{name}-includes.patch
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
%patch0 -p1

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
