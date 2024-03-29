import React from "react";
import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer className='bg-gray-800 pt-10 sm:mt-10'>
      <div className='max-w-6xl m-auto text-gray-800 flex flex-wrap justify-left'>
        <div className='p-5 w-1/2 sm:w-4/12 md:w-3/12'>
          <div className='text-xs uppercase text-gray-400 font-medium mb-6'>
            Quick Links
          </div>
          <Link className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Home
          </Link>
          <Link className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Companies
          </Link>
          <Link className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Jobs
          </Link>
          <Link className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Employee
          </Link>
        </div>

        <div className='p-5 w-1/2 sm:w-4/12 md:w-3/12'>
          <div className='text-xs uppercase text-gray-400 font-medium mb-6'>
            Core Concepts
          </div>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Atomic Design
          </a>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            BEM Naming
          </a>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            SMACSS
          </a>
        </div>

        <div className='p-5 w-1/2 sm:w-4/12 md:w-3/12'>
          <div className='text-xs uppercase text-gray-400 font-medium mb-6'>
            Community
          </div>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            GitHub
          </a>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Discord
          </a>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Twitter
          </a>
        </div>

        <div className='p-5 w-1/2 sm:w-4/12 md:w-3/12'>
          <div className='text-xs uppercase text-gray-400 font-medium mb-6'>
            More
          </div>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Terms
          </a>
          <a
            href='/'
            className='my-3 block text-gray-300 hover:text-gray-100 text-sm font-medium duration-700'>
            Privacy Policy
          </a>
        </div>
      </div>

      <div className='pt-2'>
        <div
          className='flex pb-5 px-3 m-auto pt-5 
          border-t border-gray-500 text-gray-400 text-sm 
          flex-col md:flex-row max-w-6xl'>
          <div className='mt-2'>
            <p>© 2023 Job Board. All Rights Reserved.</p>
          </div>

          <div className='md:flex-auto md:flex-row-reverse mt-2 flex-row flex'>
            <a href='/' className='w-6 mx-1'>
              <i className='uil uil-facebook-f'></i>
            </a>
            <a href='/' className='w-6 mx-1'>
              <i className='uil uil-twitter-alt'></i>
            </a>
            <a href='/' className='w-6 mx-1'>
              <i className='uil uil-youtube'></i>
            </a>
            <a href='/' className='w-6 mx-1'>
              <i className='uil uil-linkedin'></i>
            </a>
            <a href='/' className='w-6 mx-1'>
              <i className='uil uil-instagram'></i>
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
