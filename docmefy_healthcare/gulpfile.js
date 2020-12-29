// Custom gulpfile for working with django

var gulp = require('gulp');
var sass = require('gulp-sass');
var babel = require('gulp-babel');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var cleanCSS = require('gulp-clean-css');
var postcss = require("gulp-postcss");
var autoprefixer = require('autoprefixer');
var $ = require('gulp-load-plugins')();
var cssnano = require("cssnano");
var sourcemaps = require("gulp-sourcemaps");
var browserSync = require('browser-sync').create();
var del = require('del');

var paths = {
    styles: {
        src: 'static/scss/*.scss',
        dest: 'static/dist/css/'
    },
    scripts: {
        src: 'static/js/*.js',
        dest: 'static/dist/js/'
    }
};

/* Not all tasks need to use streams, a gulpfile is just another node program
 * and you can use all packages available on npm, but it must return either a
 * Promise, a Stream or take a callback and call it
 */
function clean() {
    // You can use multiple globbing patterns as you would with `gulp.src`,
    // for example if you are using del 2.0 or above, return its promise
    return del(['dist']);
}

/*
 * Define our tasks using plain functions
 */

function style() {
    return (
        gulp.src(paths.styles.src)
            // Initialize sourcemaps before compilation starts
            .pipe(sourcemaps.init())
            .pipe(sass())
            .on("error", sass.logError)
            // Use postcss with autoprefixer and compress the compiled file using cssnano
            .pipe(postcss([autoprefixer(), cssnano()]))
            // Now add/write the sourcemaps
            .pipe(sourcemaps.write())
            .pipe(gulp.dest(paths.styles.dest))
            // Add browsersync stream pipe after compilation
            .pipe(browserSync.stream())
    );
}

function scripts() {
    return gulp.src(paths.scripts.src, { sourcemaps: false })
        .pipe(babel())
        .pipe(uglify())
        .pipe(concat('main.min.js'))
        .pipe(gulp.dest(paths.scripts.dest));
}

// Dynamic Server + watching scss/html files
function watch() {

    browserSync.init({
        proxy: "127.0.0.1:8000"
    });

    gulp.watch('static/scss/**/*.scss', style);
    gulp.watch("templates/**/*.html").on('change', browserSync.reload);
    gulp.watch('static/js/**/*.js', scripts).on('change', browserSync.reload);
}

/*
 * Specify if tasks run in series or parallel using `gulp.series` and `gulp.parallel`
 */
var build = gulp.series(clean, gulp.parallel(style, scripts), watch);

/*
 * You can use CommonJS `exports` module notation to declare tasks
 */
exports.clean = clean;
exports.styles = style;
exports.scripts = scripts;
exports.watch = watch;
exports.build = build;
/*
 * Define default task that can be called by just running `gulp` from cli
 */
exports.default = build;