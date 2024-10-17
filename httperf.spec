
Name: httperf
Version: 0.9.0
Release: 8
Summary: Popular web server benchmark
Summary(pt_BR): Popular avaliador de servidores web
Group: System/Base
License: GPLv2+
Source: %{name}-%{version}.tar.gz
BuildRequires: openssl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: https://freshmeat.net/redir/httperf/4215/url_homepage/

%description
httperf is a popular web server benchmark tool for measuring web server
performance. It provides a flexible facility for generating various HTTP
workloads and for measuring server performance. The focus of httperf is
not on implementing one particular benchmark but on providing a robust,
high-performance tool that  facilitates the construction of both micro-
and macro-level benchmarks. The three distinguishing characteristics of
httperf are its robustness, which includes the ability to generate and
sustain server overload, support for the HTTP/1.1 protocol, and its 
extensibility to new workload generators and performance measurements. 

%description -l pt_BR
O httperf é uma ferramenta para avaliação de performance em servidores web.
Ele é flexível para gerar vários tipos de testes e medir a performance do
servidor. A idéia do httperf não é implementar um teste particular mas uma
implementação saudável, uma ferramenta de alta performance que facilita a
construção de testes em micro e macro-level juntos. As características do
httperf são a robustez que incluí a opção de gerar e segurar uma sobrecarga
no servidor. Suporta HTTP/1.1 protocol, e capacidade de extensão para novos
testes de performance e geradores de carga de testes.

%prep 
%setup -q

%build
autoreconf -f -i
%configure2_5x
%make

%install 
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README NEWS ChangeLog AUTHORS TODO
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man?/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-7mdv2011.0
+ Revision: 611102
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0.9.0-6mdv2010.1
+ Revision: 537368
- rebuild

* Thu Jun 11 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.9.0-6mdv2010.0
+ Revision: 384998
- fix build using autoreconf
- fix license

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-5mdv2009.0
+ Revision: 247047
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-3mdv2008.1
+ Revision: 170890
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 19 2007 Thierry Vignaud <tv@mandriva.org> 0.9.0-2mdv2008.0
+ Revision: 41505
- fix group

* Mon May 28 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.9.0-1mdv2008.0
+ Revision: 32031
- removed buildarch for i386, as it is useable in x86_64, at least
- upgrade to 0.9.0
- ported from Conectiva to Mandriva Linux
- Import httperf





* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 14:52:34 (11845)
- Copying release 0.8-4cl to releases/ directory.

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 14:52:33 (11844)
- Copying release 0.8-4cl to pristine/ directory.

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 14:52:31 (11843)
- Imported package from snapshot.

* Tue Sep 03 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-09-03 14:52:27 (11842)
- Created package directory
