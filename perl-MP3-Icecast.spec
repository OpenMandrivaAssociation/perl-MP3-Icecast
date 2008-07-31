%define	name	perl-%{module}
%define	module	MP3-Icecast
%define	version	0.02
%define	release	%mkrel 12

Summary:	MP3::Icecast - Generate Icecast streams
Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
License: 	GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/A/AL/ALLENDAY/%{module}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-buildroot
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:  perl-MP3-Info
BuildRequires:  perl-URI
BuildArch:	noarch

Provides:      perl-mp3-icecast
Obsoletes:     perl-mp3-icecast

%description
MP3::Icecast - Generate Icecast streams, as well as M3U and PLSv2 playlists.

%prep
%setup -q -n %{module}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/MP3
%_mandir/man3/*

