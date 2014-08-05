## CloudFoundry PHP Example Application:  Prestashop

This is an example application which can be run on CloudFoundry using the [PHP Build Pack].

This is an out-of-the-box implementation of Prestashop 1.6.0.9.  It's an example of how common PHP applications can easily be run on CloudFoundry.

### Usage

1. Clone the app (i.e. this repo).

  ```bash
  git clone https://github.com/thesynapses/cf-prestashop-php-buildpack.git cf-ex-Prestashop
  cd cf-ex-Prestashop
  ```

1.  If you don't have one already, create a MySQL service.  With Pivotal Web Services, the following command will create a free MySQL database through [ClearDb].

  ```bash
  cf create-service cleardb spark my-test-mysql-db
  ```

1. Edit the manifest.yml file.  Change the 'host' attribute to something unique.  Then under "services:" change "mysql-db" to the name of your MySQL service.  This is the name of the service that will be bound to your application and thus used by Prestashop.

1. Like every normal Prestashop install, edit `config/settings.inc.php` and change the [database entries].  These should be uniqe for every installation.  You can generate these using the [Prestashop.org secret-key service].

1. Push it to CloudFoundry.

  ```bash
  cf push
  ```

  Access your application URL in the browser.  You'll see the familiar Prestashop install screen.  Setup your password and your all set.
This Application will install Prestashop under htdocs.


