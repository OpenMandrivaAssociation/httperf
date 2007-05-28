
Name: httperf
Version: 0.8
Release: %mkrel 1
Summary: It is a popular web server benchmark
Summary(pt_BR): Popular avaliador de servidores web
Group: Utilities
Group(es): Utilitarios
Group(pt_BR): Utilit�rios
License: GPL
BuildArch:i386
Source: httperf-0.8.tar.gz
BuildRequires: openssl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://freshmeat.net/redir/httperf/4215/url_homepage/

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
O httperf � uma ferramenta para avalia��o de performance em servidores web.
Ele � flex�vel para gerar v�rios tipos de testes e medir a performance do
servidor. A id�ia do httperf n�o � implementar um teste particular mas uma
implementa��o saud�vel, uma ferramenta de alta performance que facilita a
constru��o de testes em micro e macro-level juntos. As caracter�sticas do
httperf s�o a robustez que inclu� a op��o de gerar e segurar uma sobrecarga
no servidor. Suporta HTTP/1.1 protocol, e capacidade de extens�o para novos
testes de performance e geradores de carga de testes.

%prep 
%setup -q

%build
%configure
make

%install 
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot} 
#mkdir -p %{buildroot}/%{_bindir}/httperf
install -m744 httperf %{buildroot}/%{_bindir}/httperf

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/httperf
