import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import BorderColorOutlinedIcon from "@mui/icons-material/BorderColorOutlined";
import BusinessCenterOutlinedIcon from "@mui/icons-material/BusinessCenterOutlined";
import LogoutOutlinedIcon from "@mui/icons-material/LogoutOutlined";
import PersonOutlineOutlinedIcon from "@mui/icons-material/PersonOutlineOutlined";
import CreateNewFolderOutlinedIcon from "@mui/icons-material/CreateNewFolderOutlined";
import ContactPageOutlinedIcon from "@mui/icons-material/ContactPageOutlined";

const CompanySidebar = () => {
  return (
    <ui className='border-r border-gray-300 px-10 pb-4 pt-8 space-y-3'>
      <li className='flex items-center gap-x-3 justify-between px-12 py-3 bg-indigo-100 text-indigo-500 font-[500] rounded-lg'>
        <HomeOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full '>Dashboard</p>
      </li>
      <li className='flex items-center gap-x-3 justify-between px-12 text-indigo-950 py-3 hover:bg-indigo-100 hover:text-indigo-500 font-[500] rounded-lg'>
        <PersonOutlineOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full '>Profile</p>
      </li>
      <li className='flex items-center gap-x-3 justify-between px-12 text-indigo-950 py-3 hover:bg-indigo-100 hover:text-indigo-500 font-[500] rounded-lg'>
        <CreateNewFolderOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full'>Post New Job</p>
      </li>
      <li className='flex items-center gap-x-3 justify-between px-12 text-indigo-950 py-3 hover:bg-indigo-100 hover:text-indigo-500 font-[500] rounded-lg'>
        <ContactPageOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full'>All Applicant</p>
      </li>
      <li className='flex items-center gap-x-3 justify-between px-12 text-indigo-950 py-3 hover:bg-indigo-100 hover:text-indigo-500 font-[500] rounded-lg'>
        <BusinessCenterOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full '>Manage Jobs</p>
      </li>
      <li className='flex items-center gap-x-3 justify-between px-12 text-indigo-950 py-3 hover:bg-indigo-100 hover:text-indigo-500 font-[500] rounded-lg'>
        <LockOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full'>Change Password</p>
      </li>
      <li className='flex items-center gap-x-3 justify-between px-12 text-indigo-950 py-3 hover:bg-indigo-100 hover:text-indigo-500 font-[500] rounded-lg'>
        <LogoutOutlinedIcon sx={{ fontSize: 25 }} />
        <p className='mr-auto min-w-full '>Logout</p>
      </li>
    </ui>
  );
};

export default CompanySidebar;
