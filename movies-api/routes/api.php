<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\MoviesController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('movie', 'App\Http\Controllers\MoviesController@index');// Mostrar todos los registros de peliculas
Route::post('movie', 'App\Http\Controllers\MoviesController@store');// Crear todos los registros de peliculas
Route::put('movie/{id}', 'App\Http\Controllers\MoviesController@update');// Actualiza
Route::delete('movie/{id}', 'App\Http\Controllers\MoviesController@destroy');//Borra