export default function NavBar() {
  return (
    <main className="grid grid-cols-5 w-screen inset-x-0 top-0 fixed place-items-center items-center p-8">
      <div className="text-center hover:text-indigo-400 hover:bold hover:scale-105 transition duration-300 ease-in-out">
        Home
      </div>
      <div className="text-center">About</div>
      <div className="text-center">Projects</div>
      <div className="text-center">Experiences</div>
      <div className="text-center">Contact</div>
    </main>
  );
}
