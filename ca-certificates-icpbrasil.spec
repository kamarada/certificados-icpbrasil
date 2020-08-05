Name:           ca-certificates-icpbrasil
Version:        2020.01.09
Release:        3
# Arquivos baixados em: https://www.iti.gov.br/repositorio/84-repositorio/489-certificados-das-acs-da-icp-brasil-arquivo-unico-compactado
# Atualizados em: 09 de janeiro de 2020
Summary:        Certificados das ACs da ICP-Brasil
License:        GPL-2.0+
Group:          Productivity/Networking/Security
Url:            https://github.com/kamarada/certificados-icpbrasil/
Source:         https://github.com/kamarada/certificados-icpbrasil/archive/15.1-dev.tar.gz#/certificados-icpbrasil.tar.gz

BuildArch:      noarch
BuildRequires:  unzip

Requires:       mozilla-nss-tools
Requires:       openssl

Requires(post):     ca-certificates
Requires(postun):   ca-certificates


%description
Este pacote contém todos os certificados das ACs da ICP-Brasil.

Para instalar os certificados no seu perfil de usuário, execute o comando:

$ instalar-icpbrasil

Para mais informações sobre esse comando, execute:

$ instalar-icpbrasil --ajuda

Esse script suporta:

- o navegador Mozilla Firefox
- os navegadores Google Chrome/Chromium
- quaisquer navegadores baseados nos supracitados (Opera, Vivaldi, Brave, etc)
- o cliente de e-mail Mozilla Thunderbird

Para navegadores instalados após este pacote, pode ser necessário executar esse
comando novamente.

Para novos usuários criados após a instalação deste pacote, os certificados são
instalados automaticamente nos navegadores Google Chrome/Chromium e derivados.

Esse script deve ser executado para cada usuário no computador (não há como
instalar os certificados em todos os navegadores a nível de sistema).


%prep
%setup -q -n certificados-icpbrasil
sha512sum -c hashsha512.txt
unzip ACcompactado.zip


%build


%install
mkdir -p %{buildroot}%{_datadir}/icpbrasil/
install -D -m 644 *.crt %{buildroot}%{_datadir}/icpbrasil/

mkdir -p %{buildroot}%{_datadir}/pki/trust/anchors/
for certificado in *.crt
do
    ln -s "%{_datadir}/icpbrasil/$certificado" "%{buildroot}%{_datadir}/pki/trust/anchors/$certificado"
done

mkdir -p %{buildroot}%{_bindir}/
install -D -m 555 instalar-icpbrasil %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -D -m 644 icpbrasil.sh %{buildroot}%{_sysconfdir}/profile.d/


%post
update-ca-certificates || true


%postun
update-ca-certificates || true


%files
%defattr(-,root,root)
%config %{_sysconfdir}/profile.d/icpbrasil.sh
%{_bindir}/instalar-icpbrasil
%{_datadir}/icpbrasil/
%{_datadir}/pki/trust/anchors/*.crt


%changelog

