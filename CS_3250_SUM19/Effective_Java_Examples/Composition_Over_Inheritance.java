

// Wrapper class - uses composition in place of inheritance
public class InstrumentedSet<E> extends ForwardingSet<E> {
	private int addCount = 0;
	public InstrumentedSet (Set<E> s){
		super(s)
	}

	@Override
	public boolean add(E e){
		addCount++;
		return super.add(e);
	}

	@Override
	public boolean addAll (Collection< ? extends E> c){
		addCount += c.size();
		return super.addAll(c);
	}

	public int getAddCount() {
		return addCount;
	}
}

// Reusable forwarding class
public class ForwardingSet<E> implements Set<E> {
	private final Set<E> s; // Composition
	public ForwardingSet(Set<E> s) { this.s = s ; }

	public void clear() {s.clear();}
	public boolean contains(Object o) { return s.contains(o);}
	public boolean isEmpty() {return s.isEmpty();}
	...
}