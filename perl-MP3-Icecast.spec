%define	upstream_name	 MP3-Icecast
%define	upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	MP3::Icecast - Generate Icecast streams
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AL/ALLENDAY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MP3::Info)
BuildRequires:	perl(URI)
BuildArch:	noarch

%rename	perl-mp3-icecast

%description
MP3::Icecast - Generate Icecast streams, as well as M3U and PLSv2 playlists.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/MP3
%{_mandir}/man3/*


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 407808
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-12mdv2009.0
+ Revision: 257923
- rebuild
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-9mdv2008.1
+ Revision: 136291
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-9mdv2008.0
+ Revision: 86671
- rebuild


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 23:21:05 (53744)
- test in %%check
- rebuild

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 23:18:35 (53743)
Import perl-MP3-Icecast

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-7mdk
- Fix File section to own the directory

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-6mdk
- Rebuild

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-5mdk
- Use good name

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-4mdk
- Fix url

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-3mdk
- Fix BuildRequires
- %%mkrel

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.02-2mdk
- rebuild for new perl

* Mon Apr 19 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.02-1mdk
- initial spec

