import Link from "next/link";

export default function NavBar() {
  const linkClasses =
    "relative text-center px-4 py-2 transition duration-300 ease-in-out text-spotlight text-spotlight-hover hover:text-indigo-400";

  return (
    <nav className="grid grid-cols-5 w-screen inset-x-0 z-50 top-0 fixed place-items-center items-center p-8">
      <Link href="/" className={linkClasses}>
        Home
      </Link>
      <Link href="/about" className={linkClasses}>
        About
      </Link>
      <Link href="/projects" className={linkClasses}>
        Projects
      </Link>
      <Link href="/experiences" className={linkClasses}>
        Experiences
      </Link>
      <Link href="/contact" className={linkClasses}>
        Contact
      </Link>
    </nav>
  );
}
