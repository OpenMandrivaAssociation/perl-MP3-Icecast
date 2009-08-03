%define	upstream_name	 MP3-Icecast
%define	upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	MP3::Icecast - Generate Icecast streams
License: 	GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AL/ALLENDAY/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:  perl-MP3-Info
BuildRequires:  perl-URI
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

Provides:      perl-mp3-icecast
Obsoletes:     perl-mp3-icecast

%description
MP3::Icecast - Generate Icecast streams, as well as M3U and PLSv2 playlists.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
