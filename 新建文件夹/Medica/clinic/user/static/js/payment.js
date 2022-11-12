var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {
  $scope.f4 = '';
  $scope.s4 = '';
  $scope.t4 = '';
  $scope.l4 = '';
  $scope.hname = '';
  $scope.edm = '';
  $scope.edy = '';
  $scope.cvv = '';
});

$('.twin input')
  .on('focus', function () {
    $(this).parent().addClass('focusit');
  })
  .blur(function () {
    $(this).parent().removeClass('focusit');
  });

$('.four-num input[ng-model="f4"]').on('keyup change', function () {
  if ($(this).val().slice(0, 1) === '4') {
    $('.logo b').attr('class', 'visa');
    $('.clayout').addClass('blueit');
  } else {
    $('.logo b').attr('class', 'master');
    $('.clayout').removeClass('blueit');
  }
});
$('.four-num input').on('keyup change', function () {
  $in = $(this);
  if ($in.val().length > 3) {
    $in.next().focus();
  }
});
$('input[ng-model="cvv"]')
  .on('focus', function () {
    $('#payment .card').addClass('flip');
  })
  .on('blur', function () {
    $('#payment .card').removeClass('flip');
  });
$('.twin input').on('keyup change', function () {
  $in = $(this);
  if ($in.next().length) {
    if ($in.val().length > 1) {
      $in.next().focus();
    }
  } else {
    if ($in.val().length > 1) {
      $in.blur();
    }
  }
});
